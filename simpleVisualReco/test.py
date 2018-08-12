from watson_developer_cloud import VisualRecognitionV3


apikey='hnueCLEXY6CoW_-qM2jucYcAmeLbCw--horse0xcy'

print( "1")
results=[]
thresh='0.6'
waitTime=15.0
#visual_recognition = VisualRecognitionV3( version='2016-05-20',
visual_recognition = VisualRecognitionV3( version='2018-03-19',
               url='https://gateway.watsonplatform.net/visual-recognition/api',
               iam_api_key=apikey)
print ("2")
print (visual_recognition)
with open('boil.jpeg', 'rb') as image_file:
      print (image_file)
      classes = visual_recognition.classify(images_file=image_file,
                                            threshold=thresh)
      #print (classes)
      score=0
      bestClass = ' '
      for a in classes['images'][0]['classifiers'][0]['classes']:

        val  = float(a['score'])

        print(a['score'] , val)
        if score < val:
           score = val
           bestClass = a['class']

        #print(a['class'] , a['score']   )
        #results.append(a['class'])
score = round(score,2) * 100
print ("Best match", bestClass , "With a confidence of ", score)

