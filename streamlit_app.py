import imghdr
import io
import json
import os
import sys
import tempfile
import time
import uuid
import zipfile
from pathlib import Path

import streamlit as st
from PIL import Image
from dotenv import load_dotenv
from gotipy import Gotify
from loguru import logger
from rembg.bg import remove  # noqa


def remove_bg(bytes_data, path):
    result = remove(bytes_data)
    img = Image.open(io.BytesIO(result)).convert('RGBA')
    # img = Image.open(io.BytesIO(bytes_data)).convert('RGBA')  # debug
    if path.suffix != '.png':
        img.LOAD_TRUNCATED_IMAGES = True
    return img


def main():
    if GOTIFY:
        g = Gotify(host_address=os.getenv('GOTIFY_HOST_ADDRESS'),
                   fixed_token=os.getenv('GOTIFY_APP_TOKEN'),
                   fixed_priority=9)

    if st.sidebar.button('CLEAR'):
        st.session_state['key'] = K
        st.experimental_rerun()
    st.sidebar.markdown('---')

    accepted_type = ['png', 'jpg', 'jpeg']
    uploaded_files = st.sidebar.file_uploader('Choose a file',
                                              type=accepted_type,
                                              accept_multiple_files=True,
                                              key=st.session_state['key'])

    if len(uploaded_files) > MAX_FILES != -1:
        st.warning(
            f'Maximum number of files reached! Only the first {MAX_FILES} '
            'will be processed.'
        )
        uploaded_files = uploaded_files[:MAX_FILES]

    if uploaded_files:
        logger.info(f'Uploaded the following files: {uploaded_files}')

        progress_bar = st.empty()
        down_btn = st.empty()
        cols = st.empty()
        col1, col2 = cols.columns(2)
        imgs_bytes = []

        for uploaded_file in uploaded_files:

            bytes_data = uploaded_file.getvalue()

            if imghdr.what(file='', h=bytes_data) not in accepted_type:
                st.error(f'`{uploaded_file.name}` is not a valid image!')
                continue

            if 'btn' not in st.session_state:
                st.session_state.my_button = True
                imgs_bytes.append((uploaded_file, bytes_data))

        col1.image([x[1] for x in imgs_bytes])

        nobg_imgs = []
        if st.sidebar.button('Remove background'):
            if GOTIFY:
                files_dicts = [x.__dict__ for x in uploaded_files]
                g.push(  # noqa
                    'New Request', json.dumps(files_dicts, indent=4))

            pb = progress_bar.progress(0)

            with st.spinner('Wait for it...'):
                for n, (uploaded_file, bytes_data) in enumerate(imgs_bytes,
                                                                start=1):
                    p = Path(uploaded_file.name)
                    img = remove_bg(bytes_data, p)
                    with io.BytesIO() as f:
                        img.save(f, format='PNG', quality=100, subsampling=0)
                        data = f.getvalue()
                    nobg_imgs.append((img, p, data))

                    cur_progress = int(100 / len(uploaded_files))
                    pb.progress(cur_progress * n)
                time.sleep(1)
                progress_bar.empty()
                pb.success('Complete!')

                col2.image([x[0] for x in nobg_imgs])

            if len(nobg_imgs) > 1:
                with io.BytesIO() as tmp_zip:
                    with zipfile.ZipFile(tmp_zip, 'w') as z:
                        for img, p, data in nobg_imgs:
                            with tempfile.NamedTemporaryFile() as fp:
                                img.save(fp.name, format='PNG')
                                z.write(fp.name,
                                        arcname=p.name,
                                        compress_type=zipfile.ZIP_DEFLATED)
                    zip_data = tmp_zip.getvalue()

                down_btn.download_button(
                    label='Download all results',
                    data=zip_data,
                    file_name=f'results_{int(time.time())}.zip',
                    mime='application/zip',
                    key='btn')
            else:
                try:
                    out = nobg_imgs[0]
                    down_btn.download_button(
                        label='Download result',
                        data=out[-1],
                        file_name=f'{out[1].stem}_nobg.png',
                        mime='image/png',
                        key='btn')
                except IndexError:
                    st.error('No more images to process!')
                finally:
                    st.session_state['key'] = K


if __name__ == '__main__':
    st.set_page_config(page_title='Remove Background',
                       page_icon='✂️',
                       initial_sidebar_state='expanded')
    st.markdown(
        '<style> footer {visibility: hidden;}'
        '#MainMenu {visibility: hidden;}</style>',
        unsafe_allow_html=True)
    logger.add('logs.log')

    load_dotenv()

    if len(sys.argv) > 1:
        MAX_FILES = int(sys.argv[1])
    elif os.getenv('MAX_FILES'):
        MAX_FILES = int(os.getenv('MAX_FILES'))
    else:
        MAX_FILES = 10

    GOTIFY = False
    if os.getenv('GOTIFY_HOST_ADDRESS') and os.getenv('GOTIFY_APP_TOKEN'):
        GOTIFY = True

    K = str(uuid.uuid4())
    if 'key' not in st.session_state:
        st.session_state['key'] = K

    main()
