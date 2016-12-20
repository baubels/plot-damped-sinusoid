from flask_wtf import FlaskForm
from wtforms import Form, FloatField, BooleanField, validators
from math import pi
import functools

def checkT(form,field):
    w=form.w.data
    T=field.data
    period=2*pi/w

    if T>30*period:
        num_periods=int(round(T/period))
        raise validators.ValidationError('Cannot plot as much as %d periods! T<%.2f' %(num_periods,30*period))

def checkInterval(form,field,min_val=None, max_val=None):
    failure = False
    if min_val is not None:
        if field.data < min_val:
            failure = True
    if max_val is not None:
        if field.data > max_val:
            failure = True
    if failure:
        raise validators.ValidationError(
        '%s = %s not in [%s, %s]' %(field.name, field.data,
        '-infty' if min_val is None else str(min_val),
        'infty' if max_val is None else str(max_val)))

def interval(min_val=None, max_val=None):
    return functools.partial(checkInterval,min_val=min_val, max_val=max_val)

class InputForm(FlaskForm):
    A=FloatField(label='amplitude (m)', default=1.0, validators=[validators.InputRequired()])
    b=FloatField(label='damping factor (kg/s)', default=2.0, validators=[validators.InputRequired(), interval(0,None)])
    w=FloatField(label='frequency (1/s)', default=3.0, validators=[validators.InputRequired()])
    T=FloatField(label='time (s)', default=10.0, validators=[validators.InputRequired(),checkT])
    SVG=BooleanField('')
