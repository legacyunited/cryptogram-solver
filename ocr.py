def detect_text(path):
    """Detects text in the file."""
    from google.cloud import vision
    import io
    import json
    client = vision.ImageAnnotatorClient.from_service_account_json('vision_api.json')

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations[0].description
    try:
        texts = ' '.join(texts.replace("\n", " ").split(' ')[1:])
        texts = ''.join([i for i in texts if not i.isdigit()])
    except:
        texts = 'Error in OCR.'

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

    if not len(texts):
        return 'No text found.'
    return texts

if __name__ == '__main__':
    detect_text('test_image_2.jpg')