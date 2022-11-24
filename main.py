from flask_restful import Resource, reqparse
import pandas as pd
import json
import boto3
from boto3.dynamodb.conditions import key, Attr
import os
import requests


class Payload(Resource):

    def __init__(self):
        """This is a payload""" 
        parser = reqparse.RequestParser()
        self.metricname = parser.add_argument("metricname", type=str, required=True, 
                                                help="This should be a platform")
        self.content_partner = parser.add_argument("content_partner", action="append", type=str, required=False,
                                                help="This should be a content_partner")
        self.device_model = parser.add_argument("device_model", action="append", type=str, required=False,
                                                help="This should be a content_type")
        self.device_platform = parser.add_argument("device_platform", action="append", type=str, required=False,
                                                help="This should be a error_type")

        self.content_type = parser.add_argument("content_type", action="append", type=str, required=False,
                                                help="This should be a location")
        self.cdn = parser.add_argument("cdn", action="append", type=str, required=False,
                                                help="This should be a location")
        self.location = parser.add_argument("location", action="append", type=str, required=False,
                                                help="This should be a location")
        self.aggregation_interval = parser.add_argument("aggregation_interval", action="append", type=str, required=False,
                                                help="This should be a location")
        self.data = parser.parse_args()
        self.m_name = self.data.get("metricname", None)
        self.con_partner = self.data.get("content_partner", None)
        self.dev_model = self.data.get("device_model", None)
        self.dev_plat = self.data.get("device_platform", None)
        self.con_type = self.data.get("content_type", None)
        self.cd_n = self.data.get("cdn", None)
        self.lo_cation = self.data.get("location", None)
        self.agg_interval = self.data.get("aggregation_interval", None)


class Mulitiselection(Payload):

    def __init__(self):
        super().__init__()
        self.m_name = self.m_name
        self.con_partner = self.con_partner
        self.dev_model = self.dev_model
        self.dev_plat = self.dev_plat
        self.con_type = self.con_type
        self.cd_n = self.cd_n
        self.lo_cation = self.lo_cation
        self.agg_interval = self.agg_interval




