from marshmallow import Schema, fields, validate


class DreamSchema(Schema):
    id = fields.Integer(dump_only=True)
    owner_id = fields.Integer()
    name = fields.String(required=True)
    description = fields.String()
    image_link = fields.String()
    store_link = fields.String()
    is_fulfilled = fields.Boolean()
    message = fields.String(dump_only=True)


class UserSchema(Schema):
    id = fields.Integer(dump_only=True)
    email = fields.String(required=True, validate=[
        validate.Length(max=100)
    ])
    password = fields.String(required=True, load_only=True)
    username = fields.String(required=True, validate=[
        validate.Length(max=50)
    ])
    name = fields.String(required=True, validate=[
        validate.Length(max=50)
    ])
    surname = fields.String(required=True, validate=[
        validate.Length(max=50)
    ])
    birthday = fields.Date()
    dreams = fields.Nested(DreamSchema, many=True, dump_only=True)
    # gifts
    # friends
    # friend_requests


class AuthSchema(Schema):
    access_token = fields.String(dump_only=True)
    message = fields.String(dump_only=True)
