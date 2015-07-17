__author__ = 'jason'

from _collections import *
import datetime

def insert_group(name, institution):

    g = Groups(name=name, institution=institution)
    g.save()
    return g

def insert_scientist(name, email, phone, group):

    s = Scientists(name=name, email=email, phone=phone, group=group)
    s.save()
    return s

def insert_process(name, amount, composition, CAS_number):

    p = Processes(name=name, amount=amount, compostion=composition,
                  CAS_number=CAS_number)
    p.save()
    return p

def insert_support(name, details):

    s = Support(name=name, details=details)
    s.save()
    return s

def insert_characterization(name, details):

    c = Characterization(name=name, details=details)
    c.save()
    return c

def insert_hazard(ignitable, corrosive, reactive, poisonous):

    h = Hazards(ignitable=ignitable, corrosive=corrosive,
                reactive=reactive, poisonous=poisonous)
    h.save()
    return h

def insert_product(composition, notebook_reference, date=datetime.datetime.now):

    sp = SyntheticProducts(composition=composition, date=date,
                           notebook_reference=notebook_reference)
    sp.save()
    return sp

def insert_sample(concentration, comments, scientist, product,
                  support, characterization, hazards, process):

    s = Samples(concentration=concentration, comments=comments, scientist=scientist,
                product=product, support=support, characterization=characterization,
                hazards=hazards, process=process)
    s.save()
    return s

def insert_shipment(date, recipient, scientist, address):

    sh = Shipments(date=date, recipient=recipient, scientist=scientist,
                   address=address)
    sh.save()
    return sh

def insert_vial(amount, concentration, quanity, sample, shipment):

    v = Vials(amount=amount, concentration=concentration, quanity=quanity,
              sample=sample, shipment=shipment)
    v.save()
    return v

def insert_exp_type(type):

    t = ExperimentType(type=type)
    t.save()
    return t

def insert_planned_exp(type, priority, planned_date, scientist):

    pexp = PlannedExperiments(type=type, priority=priority,
                              planned_date=planned_date, scientist=scientist)
    pexp.save()
    return pexp

def insert_ran_exp(plan, scientist, images):

    rexp = RanExperiments(plan=plan, scientist=scientist, images=images)
    rexp.save()
    return rexp

def insert_data_processing(experiments, software_version, kwargs, processed_data,
                           procedure):

    dp = DataProcessing(experiments=experiments, software_version=software_version,
                        kwargs=kwargs, processed_data=processed_data,
                        procedure=procedure)
    dp.save()
    return dp

def insert_sim(starting_atoms, finished_atoms, calculator, data):

    si = Simulations(starting_atoms=starting_atoms, finished_atoms=finished_atoms,
                     calculator=calculator, data=data)
    si.save()
    return si