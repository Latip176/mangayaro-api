class FinalOutput:
    def results(self, data, msg, status_code) -> dict:
        return {
        	"results": [{"data": data, "msg": msg, "status_code": status_code}],
        	"author": "Latip176",
        }
