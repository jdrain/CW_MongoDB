__author__ = 'jason'

from tables import *
import datetime

def insert_group(name, institution):

    time = datetime.datetime.now()
    g = Groups(name=name, institution=institution, time=time)
    g.save()
    return g

def insert_scientist(name, email, phone, group):

    time = datetime.datetime.now()
    s = Scientists(name=name, email=email, phone=phone, group=group, time=time)
    s.save()
    return s

def insert_process(name, amount, composition, CAS_number):

    time = datetime.datetime.now()
    p = Processes(name=name, amount=amount, compostion=composition,
                  CAS_number=CAS_number, time=time)
    p.save()
    return p

def insert_support(name, details):

    time = datetime.datetime.now()
    s = Support(name=name, details=details, time=time)
    s.save()
    return s

def insert_characterization(name, details):

    time = datetime.datetime.now()
    c = Characterization(name=name, details=details, time=time)
    c.save()
    return c

def insert_hazard(ignitable, corrosive, reactive, poisonous):

    time = datetime.datetime.now()
    h = Hazards(ignitable=ignitable, corrosive=corrosive,
                reactive=reactive, poisonous=poisonous, time=time)
    h.save()
    return h

def insert_product(composition, notebook_reference, date=datetime.datetime.now):

    time = datetime.datetime.now()
    sp = SyntheticProducts(composition=composition, date=date,
                           notebook_reference=notebook_reference, time=time)
    sp.save()
    return sp

def insert_sample(concentration, comments, scientist, product,
                  support, characterization, hazards, process):

    time = datetime.datetime.now()
    s = Samples(concentration=concentration, comments=comments, scientist=scientist,
                product=product, support=support, characterization=characterization,
                hazards=hazards, process=process, time=time)
    s.save()
    return s

def insert_shipment(date, recipient, scientist, address):

    time = datetime.datetime.now()
    sh = Shipments(date=date, recipient=recipient, scientist=scientist,
                   address=address, time=time)
    sh.save()
    return sh

def insert_vial(amount, concentration, quanity, sample, shipment):

    time = datetime.datetime.now()
    v = Vials(amount=amount, concentration=concentration, quanity=quanity,
              sample=sample, shipment=shipment, time=time)
    v.save()
    return v

def insert_exp_type(type):

    time = datetime.datetime.now()
    t = ExperimentType(type=type, time=time)
    t.save()
    return t

def insert_planned_exp(type, priority, planned_date, scientist):

    time = datetime.datetime.now()
    pexp = PlannedExperiments(type=type, priority=priority, time=time,
                              planned_date=planned_date, scientist=scientist)
    pexp.save()
    return pexp

def insert_ran_exp(plan, scientist, images):

    time = datetime.datetime.now()
    rexp = RanExperiments(plan=plan, scientist=scientist, images=images, time=time)
    rexp.save()
    return rexp

def insert_data_processing(experiments, software_version, kwargs, processed_data,
                           procedure):

    time = datetime.datetime.now()
    dp = DataProcessing(experiments=experiments, software_version=software_version,
                        kwargs=kwargs, processed_data=processed_data,
                        procedure=procedure, time=time)
    dp.save()
    return dp

def insert_sim(starting_atoms, finished_atoms, calculator, data):

    time = datetime.datetime.now()
    si = Simulations(starting_atoms=starting_atoms, finished_atoms=finished_atoms,
                     calculator=calculator, data=data, time=time)
    si.save()
    return si