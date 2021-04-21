def detect_text(path):
    if not path:
        return 'No path provided.'

    """Detects text in the file."""
    from google.cloud import vision
    import io
    import json
    client = vision.ImageAnnotatorClient.from_service_account_json('vision_api.json')

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)

    try:
        texts = response.text_annotations[0].description
    except:
        return 'No text found.'

    texts = ' '.join(texts.replace("\n", " ").split(' ')[1:])
    texts = ''.join([i for i in texts if not i.isdigit()])
    
    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

    return texts

if __name__ == '__main__':
    detect_text('media/test_image_2.jpg')
    detect_text('media/wallpaper2.jpg')