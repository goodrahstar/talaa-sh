import web
import classify_image_deploy



urls = (
    '/', 'index'
)

class index:
    def GET(self):
        image_name = web.input(name='grace_hopper')
        classify_image_deploy.jsonlist= []
        try:
#            img = open('/Users/rahulkumar/Downloads/'+ image_name.name +'.jpg', 'rb').read()

            output = classify_image_deploy.tf_method('/Users/rahulkumar/Downloads/'+ image_name.name +'.jpg')

        except:
            print 'Image not Found'
            output = 'Image not found'
            pass
        
        return output

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
