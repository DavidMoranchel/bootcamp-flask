from flask import request, json, Response, Blueprint

from ..models import BootcampModel
from ..schemas import BootcampListSchema, BootcampSchema

bootcamp_api = Blueprint('bootcamps', __name__)
bootcamp_list_schema = BootcampListSchema()
bootcamp_schema = BootcampSchema()

@bootcamp_api.route("/", methods=['GET'])
def get_all():
    bootcamps = BootcampModel.get_all()
    data = bootcamp_list_schema.dump(bootcamps, many=True)

    return Response(
        mimetype="application/json",
        response= json.dumps({
            'data': data
        }),
        status=200
    )

@bootcamp_api.route("/<int:bootcamp_id>/", methods=['GET'])
def retrieve(bootcamp_id):
    bootcamp = BootcampModel.get_by_id(bootcamp_id)
    if not bootcamp:
        return Response(
            mimetype="application/json",
            response=json.dumps({
                'error': "bootcamp not found"
            }),
            status=404
        ) 

    data = bootcamp_schema.dump(bootcamp)
    return Response(
        mimetype="application/json",
        response=json.dumps({
            'data': data
        }),
        status=200
    )