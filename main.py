#------------------ REST API: Postman -------------------
# from flask import Flask, jsonify, request, Response
# import json
# #from test import *
# app=Flask(__name__)
# books=[
#     {
#      'name': 'Creativity, Inc',
#      'price': 7.99,
#      'isbn': 9764847372
#      },
#     {
#      'name': 'Sapiens',
#      'price': 6.99,
#      'isbn': 9787433621
#      },
# ]

# @app.route('/books')
# def get_books():
#     return jsonify({'books':books})
# def validBookObject(bookObject):
#     if ("name" in bookObject and "price" in bookObject and "isbn" in bookObject):
#         return True
#         print("true")
#     else:
#         return False
#         print("false")
# @app.route('/books', methods=['GET','POST'])
# def add_book():
#     if request.method=='GET':
#         return jsonify({'books':books})
#     else:
#         request_data=request.get_json()
#         if(validBookObject(request_data)):
#             new_book={
#                 "name": request_data['name'],
#                 "price": request_data['price'],
#                 "isbn": request_data['isbn']
#             }
#             books.insert(0, new_book)
#             response=Response("", 201, mimetype='application/json')
#             response.headers['Location']="/books/"+str(new_book['isbn'])
#             return response
#         else:
#             invalidBookObjectErrorMsg={
#                 "error": "Invalid book object passed in request",
#                 "helpString": "Data passed in similar to this {'name':'bookname', 'price': 7.99, 'isbn':9780394800}"
#             }
#             response=Response(json.dumps(invalidBookObjectErrorMsg), status=400, mimetype='application/json');
#             return response
# @app.route('/books/<int:isbn>')
# def get_book_by_isbn(isbn):
#     return_value={}
#     for book in books:
#         if book["isbn"] == isbn:
#             return_value={
#                 'name':book["name"],
#                 'price':book["price"]
#                 }
#     return jsonify(return_value)
# def valid_put_request_data(request_data):
#     if("name" in request_data and "price" in request_data):
#         return True
#     else:
#         return False
# @app.route('/books/<int:isbn>', methods=['PUT'])
# def replace_book(isbn):
#     request_data=request.get_json()
#     if(not valid_put_request_data(request_data)):
#         invalidBookObjectErrorMsg={
#             "error": "Invalid book object passed in request",
#                 "helpString": "Data passed in similar to this {'name':'bookname', 'price': 7.99}"
#             }
#     response=Response(json.dumps(invalidBookObjectErrorMsg), status=400, mimetype='application')
#     new_book={
#         'name': request_data['name'],
#         'price': request_data['price'],
#         'isbn': isbn
#     }
#     i=0;
#     for book in books:
#         currentIsbn=book["isbn"]
#         if currentIsbn ==isbn:
#             book[i] = new_book
#         i==1
#     response= Response("", status=204)
#     return jsonify(request.get_json())
#     return 'No book with {} isbn value'.format(isbn)


# if __name__ == '__main__':
#     @app.route('/books/<int:isbn', methods=['PATCH'])
#     def update_book(isbn):
#         request_data=request.get_json()
#         updated_book={}
#         if("name" in request_data):
#             updated_book["name"]=request_data['name']
#         if("price" in request_data):
#             updated_book["price"]=request_data['price']
#         for book in books:
#             if book ["isbn"]==isbn:
#                 book.update(updated_book)
#         response=Response("", status=204)
#         response.headers['Location']="/books/"+str(isbn)
#         return response
#     #PATCH /books/975039480165
#     #{
#     # 'name':'Harry Potter'
#     # }

#     app.run(port=5000)






# ------------------------ REST API 2: GET, POST, PUT, DELETE ----------------------------------------









# from flask import Flask
# from flask_restful import Resource, Api
# app=Flask('VideoAPI')
# api=Api(app)
# videos={
#     'video1':{'title':'Python AI'},
#     'video2':{'title':'OpenAI'},
#     'video3':{'title':'TeslaAI'}
# }

# class Video(Resource):
# 	def get(self):
# 		return videos[video_id]
# api.add_resource(Video,'/videos/<video_id>')
# if __name__=='__main__':
# 	app.run()












# from flask import Flask, jsonify
# app = Flask(__name__)
# courses=[{
#       "Description":"Python in AI",
#       "course_id":"0",
#       "name":"Python AI Certificate",
#       "site":"btu.edu.ge"
#       },
#      {
#       "Description":"CCNA",
#       "course_id":"1",
#       "name":"CCNA Certificate",
#       "site":"netacad.com"
#       },
#      {
#       "Description":"Linux",
#       "course_id":"2",
#       "name":"Linux Certificate",
#       "site":"netdevgroup.com"
#  }]

# @app.route('/')
# def index():
#     return 'Python, CCNA, Linux, OpenAI'

# @app.route("/courses", methods = ['GET'])
# def get():
#     return jsonify({'Courses': courses})

# @app.route("/courses/<int:course_id>", methods = ["GET"])
# def get_course(course_id):
#     return jsonify({'course': courses[course_id]})

# @app.route("/courses", methods = ["POST"])
# def create():
#     course = {"Description":"SQLserver",
#     "course_id":"3",
#     "name":"SQLserver Certificate",
#     "site":"mygreatlearning.com"}
#     courses.append(course)
#     return jsonify({'Created': course})

# @app.route("/courses/<int:course_id>", methods = ["PUT"])
# def course_update(course_id):
#     courses[course_id]['Description'] = "TESLA OS"
#     return jsonify({'course': courses[course_id]})

# @app.route("/courses/<int:course_id>", methods = ["DELETE"])
# def delete(course_id):
#     courses.remove(courses[course_id])
#     return jsonify({'result': True})

# if __name__ == "__main__":
#     app.run(debug = True)










# ------------------ REST API 3: SQLite ------------


from flask import Flask
import dataset
app = Flask(__name__)
db = dataset.connect('sqlite:///api.db')

books={
       '1':{
           "id":"1",
           "name":"Elon Musk",
           "author":"Ashlee Vance"
           },
       '2':{
           "id":"2",
           "name":"Steve Jobs",
           "author":"Walter Isaacson"
           }
       }

table = db['books']
table.insert({
    "book_id":"1",
    "name":"Elon Musk",
    "author":"Ashlee Vance"
    })

table.insert({
    "book_id":"2",
    "name":"Steve Jobs",
    "author":"Walter Isaacson"
    })

def fetch_db(book_id):
    return table.find_one(book_id = book_id)
def fetch_db_all():
    return table.all()

@app.route('/api/books', methods = ['GET', 'POST'])
def api_books():
    if request.method == "GET":
        return make_response(jsonify(books), 200)




if __name__ == "__main__":
    app.run()