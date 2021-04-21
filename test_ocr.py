from ocr import detect_text
import pytest

def test_detect_text():
    assert detect_text('media/test_image_2.jpg') == 'PFWOKCDK VYZO WYFNPXKFWK PF VYZO DKBN-JYOMU CFX PF VYZO CTPBPMV MỸ WYFMOPTZMK IYYX MUPFID MY MUK JYOBX. -BPFXDKV DMPOBPFI -ВРЕ  '
    
    with pytest.raises(TypeError):
        detect_text()
    
    assert detect_text('media/wallpaper2.jpg') == 'No text found.'


