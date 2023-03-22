from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template

routes_report= Blueprint("routes_report",__name__)

@routes_report.route('/indexreport', methods=['GET'])
def indexreport():
    return render_template('/main/report.html')