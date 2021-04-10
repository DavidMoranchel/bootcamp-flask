from marshmallow import fields, Schema

class BootcampListSchema(Schema):
    """
    Bootcamp List Schema
    """
    id = fields.Int(required=True)
    name = fields.Str(required=True)

class BootcampSchema(Schema):
    """
    Bootcamp Schema
    """
    id = fields.Int(required=True)
    name = fields.Str(required=True)
    created_at = fields.DateTime(required=True)