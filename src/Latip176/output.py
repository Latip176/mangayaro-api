from flask import jsonify


class FinalOutput:
    def results(self, data, msg, status_code) -> dict:
        return (
            jsonify(
                {
                    "results": [
                        {"data": data, "msg": msg.lower(), "status_code": status_code}
                    ],
                    "author": "Latip176",
                }
            ),
            status_code,
        )
