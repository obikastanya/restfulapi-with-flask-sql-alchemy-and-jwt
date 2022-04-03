from flask import request
from app import app
from application.discount.discountController import DiscountController
from application.discountType.discountTypeController import DiscountTypeController
from application.user.userController import LoginController, UserController
from application.utilities.auth import  Auth

auth=Auth()

@app.route('/discount_api', methods=['GET', 'POST', 'PUT', 'DELETE'])
@auth.middleware
def discountApi():
    controller=DiscountController()
    if request.method == 'POST':
        return controller.insertNewData()
    if request.method == 'GET':
        return controller.getData()
    if request.method == 'PUT':
        return controller.updateData()
    if request.method == 'DELETE':
        return controller.deleteData()
    return {'status':False, 'msg':'ínvalid http method'}

@app.post('/discount_api_search')
@auth.middleware
def discountApiSearch():
    return DiscountController().searchSingleData()

@app.get('/discount_type_api')
@auth.middleware
def discountTypeApi():
    return DiscountTypeController().getData()

@app.post('/login')
def login():
    return LoginController().login()

@app.get('/logout')
def logOut():
    return LoginController().logOut()


@app.post('/newuser')
def newUser():
    return UserController().insertNewData()