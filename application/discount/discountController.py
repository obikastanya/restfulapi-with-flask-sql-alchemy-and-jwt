from flask import request
from .discountModel import db,Discount, DiscountSchema
from application.utilities.response import Response

class DiscountController:
    def __init__(self):
        self.dataHandler=DataHandler()
    
    def getData(self):
        try:
            data=self.dataHandler.grabData()
            return Response.make(status=True, data=data)
        except:
            return Response.make('Eror while trying to retrieve data' )

    def insertNewData(self):
        try:
            parameter={
                'msd_msdt_id':request.json.get('discount_type'),
                'msd_desc':request.json.get('discount'),
                'msd_nominal':int(request.json.get('nominal',0)),
                'msd_active_status':request.json.get('active_status','Y')
            }
            self.dataHandler.insertNewData(parameter)
            return Response.make(True,'Data successfully added' )
        except:
            return Response.make(False,'Insert data failed' )

    def updateData(self):
        try:
            parameter={
            'msd_id':request.json.get('discount_id'),
            'msd_msdt_id':request.json.get('discount_type'),
            'msd_desc':request.json.get('discount'),
            'msd_nominal':int(request.json.get('nominal',0)),
            'msd_active_status':request.json.get('active_status','Y')
            }
            self.dataHandler.updateData(parameter)
            return Response.make(True, 'Data successfully updated' )
        except:
            return Response.make(False,'Update data failed' )

    def deleteData(self):
        try:
            parameter={
            'msd_id':request.json.get('discount_id')
            }
            self.dataHandler.deleteData(parameter)
            return Response.make(True,'Data successfully removed' )
        except:
            return Response.make('Data failed to removed' )

    def searchSingleData(self):
        try:
            parameter={'msd_id':request.json.get('discount_id')}
            singleData=self.dataHandler.grabSingleData(parameter)
            return Response.make(msg='Data Found', data=singleData)
        except:
            return Response.make(False,'Cant find data' )

class DataHandler:
    def __init__(self):
        self.Model=Discount
        self.Schema=DiscountSchema

    def grabData(self):
        objectResults=self.Model.query.all()
        return self.Schema(many=True).dump(objectResults)
    
    def insertNewData(self,parameter):
        objectToInsert=self.Model(**parameter)
        db.session.add(objectToInsert)
        db.session.commit()

    def updateData(self, parameter):
        discount=self.grabOne(parameter)
        discount.msd_msdt_id=parameter.get('msd_msdt_id')
        discount.msd_desc=parameter.get('msd_desc')
        discount.msd_nominal=parameter.get('msd_nominal')
        discount.msd_active_status=parameter.get('msd_active_status')
        db.session.commit()
    
    def deleteData(self, parameter):
        objectToDelete=self.grabOne(parameter)
        db.session.delete(objectToDelete)
        db.session.commit()
    
    def grabOne(self, parameter):
        return self.Model.query.filter(self.Model.msd_id==parameter.get('msd_id')).first()
