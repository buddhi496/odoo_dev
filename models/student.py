from odoo import api, models, fields


class Schoolnts(models.Model):
    _name = "school.students"
    _description = "School Student Record"

    name = fields.Char(striStudeng="First Name", required=True)
    mname = fields.Char(string="Middle Name", required=True)
    lname = fields.Char(string="Last Name", required=True)
    image = fields.Binary(string="Image", help="Select image here")
    clas = fields.Many2one('school.class', string="Class")
    roll = fields.Integer(string="Roll No.", required=True)
    mobile = fields.Integer(string="Contact")
    section = fields.Char(string="Section", required=True)

    occupation = fields.Char(string="Occupation", required=True)
    address = fields.Char(string="Address", required=True)
    nam = fields.Char(string="Name", required=True)
    mobil = fields.Integer(string="Contact")

    occ = fields.Char(string="Occupation", required=True)
    add = fields.Char(string="Address", required=True)
    na= fields.Char(string="Name", required=True)
    mobi = fields.Integer(string="Contact")


    fstreet = fields.Char(string="First Street Name")
    sstreet = fields.Char(string="Second Street Name")
    palika = fields.Char(string="Palika")
    district = fields.Char(string="District")
    state = fields.Char(string="State")
    country = fields.Char(string="Country")
    zip = fields.Char(string="Zip Code")

    ffstreet = fields.Char(string="First Street Name")
    fsstreet = fields.Char(string="Second Street Name")
    fpalika = fields.Char(string="Palika")
    fdistrict = fields.Char(string="District")
    fstate = fields.Char(string="State")
    fcountry = fields.Char(string="Country")
    fzip = fields.Char(string="Zip Code")

class SchoolClass(models.Model):
    _name = "school.class"
    _description = "School class Record"

    name = fields.Char(string="Name", required=True)
    clas = fields.Char(string="Class", required=True)


class SchoolSection(models.Model):
    _name = "school.section"
    _description = "School section Record"

    clas = fields.Char(string="Class", required=True)
    section = fields.Char(string="Section", required=True)







