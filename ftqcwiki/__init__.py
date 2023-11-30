#!/usr/bin/env python3
import base64
from io import BytesIO
from qiskit import qasm3


def _fig_to_base64(fig):
    picture_file = BytesIO()
    fig.savefig(picture_file, format="png")
    picture_file.seek(0)
    return base64.b64encode(picture_file.read()).decode("ascii")

def format_openqasm(source, language, css_class, options, md, **kwargs):
    print(source)
    try:
        qc = qasm3.loads(source)
        base64 = _fig_to_base64(qc.draw(output="mpl", style="iqp"))

        return f"<img src='data:image/png;base64,{base64}'>"
    
    except Exception as e:
        print(e)
    return "test"
