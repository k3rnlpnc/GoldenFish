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


class UserSchema(Schema):
    id = fields.Integer()
    email = fields.String(validate=[
        validate.Length(max=100)
    ])
    password = fields.String(required=True, load_only=True)
    username = fields.String(validate=[
        validate.Length(max=50)
    ])
    name = fields.String(validate=[
        validate.Length(max=50)
    ])
    surname = fields.String(validate=[
        validate.Length(max=50)
    ])
    birthday = fields.Date()
    dreams = fields.Nested(DreamSchema, many=True, dump_only=True)


class AuthSchema(Schema):
    access_token = fields.String(dump_only=True)
    message = fields.String(dump_only=True)


class UserPageSchema(Schema):
    user = fields.Nested(UserSchema(only=('id', 'username', 'name', 'surname', 'birthday')), many=False)
    dreams = fields.Nested(DreamSchema(only=('id', 'name', 'giver_username', 'giver_id')), many=True)
