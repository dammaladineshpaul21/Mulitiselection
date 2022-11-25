from flask_restful import Resource, reqparse


class Payload(Resource):

    def __init__(self):
        """This is a payload"""
        parser = reqparse.RequestParser()
        self.location = parser.add_argument("location", action="append", type=str, required=True,
                                            help="This should be a location")
        self.content_type = parser.add_argument("content_type", action="append", type=str, required=False,
                                                help="This should be a content_type")
        self.provider = parser.add_argument("provider", action="append", type=str, required=False,
                                            help="This should be a provider")
        self.platfrom = parser.add_argument("platfrom", action="append", type=str, required=False,
                                            help="This should be a platfrom")

        self.error_code = parser.add_argument("error_code", action="append", type=str, required=False,
                                              help="This should be a error_code")
        self.data = parser.parse_args()
        self._location = self.data.get("location", None)
        self._content_type = self.data.get("content_type", None)
        self._provider = self.data.get("provider", None)
        self._platfrom = self.data.get("platfrom", None)
        self._error_code = self.data.get("error_code", None)


class Mulitiselection(Payload):

    def __init__(self):
        super().__init__()
        self.m_name = self._location
        self.con_partner = self._content_type
        self.dev_model = self._provider
        self.dev_plat = self._platfrom
        self.con_type = self._error_code

    def post(self):
        return {"location": self.m_name,
                "content_type": self.con_partner,
                "provider": self.dev_model,
                "platfrom": self.dev_plat,
                "error_code": self.con_type}


