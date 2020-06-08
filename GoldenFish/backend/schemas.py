from marshmallow import Schema, fields, validate


class DreamSchema(Schema):
    id = fields.Integer()
    owner_id = fields.Integer()
    name = fields.String()
    description = fields.String()
    image_link = fields.String()
    store_link = fields.String()
    is_fulfilled = fields.Boolean()
    giver_id = fields.Integer()
    giver_username = fields.String()
    message = fields.String(dump_only=True)


class GiftSchema(Schema):
    id = fields.Integer(dump_only=True)
    dream_id = fields.Integer(required=True)
    giver_id = fields.Integer(required=True)
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


class AuthSchema(Schema):
    access_token = fields.String(dump_only=True)
    message = fields.String(dump_only=True)
