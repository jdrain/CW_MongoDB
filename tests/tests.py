__author__ = 'jason'

from connection import *
from insert import *
import mongoengine

def conn():
    con = db_connect('testdb')
    return con

def disconn():
    d = mongoengine.connection.disconnect(DB_ALIAS)
    return d

def ins_group():
    #test insertion of a group object
    g = insert_group(name='test', institution='test')
    g1 = Groups.objects(name=g.name)
    print g1

def ins_scientist():
    s = insert_scientist(name='test', email='test', phone='test', group='test')
    s1 = Scientists.objects(name=s.name)
    return s1

def ins_process():
    p = insert_process(name='test',amount='test', composition='test', CAS_number='test')
    p1 = Processes.objects(name=p.name)
    return p1

def ins_support():
    s = insert_support(name='test', details='test')
    s1 = Support.objects(name=s.name)
    return s1

def ins_characterization():
    c = insert_characterization(name='test', details='test')
    c1 = Characterization.objects(name=c.name)
    return c1

def ins_hazard():
    h = insert_hazard(ignitable='test', reactive='test', corrosive='test', poisonous='test')
    h1 = Hazards.objects(ignitable=h.ignitable)
    return h1

def ins_product():
    p = insert_product(composition='test', notebook_reference='test')
    p1 = SyntheticProducts.objects(composition=p.composition)
    return p1

def ins_sample():
    s = insert_sample(concentration='test', comments='test', scientist='test', product='test',
                      support='test', characterization='test', hazards='test', process='test')
    s1 = Samples.objects(comments=s.comments)
    return s1

def ins_shipment():
    s = insert_shipment(date='test', recipient='test', scientist='test', address='test')
    s1 = Shipments.objects(recipient=s.recipient)
    return s1

def ins_vial():
    v = insert_vial(amount='test', concentration='test', shipment='test', quantity='test', sample='test')
    v1 = Vials.objects(sample=v.sample)
    return v1

def ins_exp_type():
    e = insert_exp_type(type='test')
    e1 = ExperimentType.objects(type=e.type)
    return e1

def ins_planned_exp():
    p = insert_planned_exp(type='test', priority='test', planned_date='test', scientist='test')
    p1 = PlannedExperiments.objects(type=p.type)
    return p1

def ins_ran_exp():
    e = insert_ran_exp(plan='test', scientist='test', images='test')
    e1 = RanExperiments.objects(images=e.images)
    return e1

def ins_data_pro():
    dp = insert_data_processing(experiments='test', software_version='test', kwargs='test', processed_data='test',
                                procedure='test')
    dp1 = DataProcessing.objects(kwargs=dp.kwargs)
    return dp1

def ins_sim():
    s = insert_sim(starting_atoms='test', finished_atoms='test', calculator='test', data='test')
    s1 = Simulations.objects(data=s.data)
    return s1