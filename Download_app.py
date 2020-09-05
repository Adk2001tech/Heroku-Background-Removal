# app= Flask(__name__)

#@app.route('/Prediction', methods = ['GET', 'POST'])
#def pred():
    if request.method=='POST':
         file = request.files['file']
         org_img, feed_img= load_net.process_file(file)
         arr = load_net.out_via_model_sm(feed_img)
         arr=arr*255.0
         
         img = Image.fromarray(arr.astype('uint8'))
         file_object= BytesIO()
         img.save(file_object, format='png')
         
         file_object.seek(0)
       
         return send_file(file_object, mimetype='image/PNG',attachment_filename='pic.png',  as_attachment=True)
         
         
    #### THIS code will download the `arr` image .png file format
