from flask import Flask,Blueprint, render_template, request, redirect, url_for, flash
from flask import current_app as app
from models import *
app=Flask(__name__)

