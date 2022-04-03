from marshmallow import fields, Schema
from app import db

class DiscountType(db.Model):
    """Object for table ms_discount_type"""
    __tablename__='ms_discount_type'
    msdt_id=db.Column(db.Integer(), primary_key=True)
    msdt_desc=db.Column(db.String(200))
    msdt_active_status=db.Column(db.String(1))
    # relation config with ms_discount
    discount_type=db.relationship('Discount', backref='discount_type')

class DiscountTypeSchema(Schema):
    """Schema to retrieve data from Model Discount Type as dictionary.
    data_key is an alias for column name."""
    msdt_id=fields.Int(data_key='discount_type_id')
    msdt_desc=fields.Str(data_key='discount_type')
    msdt_active_status=fields.Str(data_key='active_status')
