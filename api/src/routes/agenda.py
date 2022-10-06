from flask import Blueprint, jsonify, request
from models import Agenda

bpAgenda = Blueprint('bpAgenda', __name__)

@bpAgenda.route('/agendas', methods=['GET'])
def all_agendas():
    agendas = Agenda.query.all()
    agendas = list(map(lambda agenda: agenda.serialize(), agendas))
    return jsonify(agendas), 200

@bpAgenda.route('/agendas/<int:id>/contacts')
def get_agenda_by_id_with_contacts(id):
    agenda = Agenda.query.get(id) # None

    if not agenda: return jsonify({ "msg": "Agenda doesn't exist!"}), 404

    return jsonify(agenda.serialize_with_contacts()), 200


@bpAgenda.route('/agendas', methods=['POST'])
def store_agenda():

    title = request.json.get('title')
    users_id = request.json.get('users_id')

    agenda = Agenda()
    agenda.title = title
    agenda.users_id = users_id
    agenda.save()

    return jsonify(agenda.serialize()), 201

@bpAgenda.route('/agendas/<int:id>/update', methods=['PUT'])
def update_agenda(id):

    title = request.json.get('title')
    users_id = request.json.get('users_id')

    agenda = Agenda.query.get(id)
    agenda.title = title
    agenda.users_id = users_id
    agenda.save()

    return jsonify(agenda.serialize()), 200

@bpAgenda.route('/agendas/<int:id>/delete', methods=['DELETE'])
def delete_agenda(id):

    agenda = Agenda.query.get(id)
    agenda.delete()

    return jsonify({ "message": "Agenda Deleted!"}), 200
