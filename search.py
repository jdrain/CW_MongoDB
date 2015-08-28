__author__ = 'jason'

from tables import *

def find_group(**kwargs):
    groups = Groups.objects(__raw__=kwargs)
    ls = [group for group in groups]
    return ls

def find_scientist(**kwargs):
    scientists = Scientists.objects(__raw__=kwargs)
    ls = [scientist for scientist in scientists]
    return ls

def find_process(**kwargs):
    processes = Processes.objects(__raw__=kwargs)
    ls = [process for process in processes]
    return ls

def find_support(**kwargs):
    supports = Support.objects(__raw__=kwargs)
    ls = [support for support in supports]
    return ls

def find_characterization(**kwargs):
    characterizations = Characterization.objects(__raw__=kwargs)
    ls = [characterization for characterization in characterizations]
    return ls

def find_hazard(**kwargs):
    hazards = Hazards.objects(__raw__=kwargs)
    ls = [hazard for hazard in hazards]
    return ls

def find_product(**kwargs):
    products = SyntheticProducts.objects(__raw__=kwargs)
    ls = [product for product in products]
    return ls

def find_sample(**kwargs):
    samples = Samples.objects(__raw__=kwargs)
    ls = [sample for sample in samples]
    return ls

def find_shipment(**kwargs):
    shipments = Shipments.objects(__raw__=kwargs)
    ls = [shipment for shipment in shipments]
    return ls

def find_vial(**kwargs):
    vials = Vials.objects(__raw__=kwargs)
    ls = [vial for vial in vials]
    return ls

def find_type(**kwargs):
    types = ExperimentType.objects(__raw__=kwargs)
    ls = [type for type in types]
    return ls

def find_planned_exp(**kwargs):
    exps = PlannedExperiments.objects(__raw__=kwargs)
    ls = [exp for exp in exps]
    return ls

def find_ran_exp(**kwargs):
    exps = RanExperiments.objects(__raw__=kwargs)
    ls = [exp for exp in exps]
    return ls

def find_data_pro(**kwargs):
    dataps = DataProcessing.objects(__raw__=kwargs)
    ls = [datap for datap in dataps]
    return ls

def find_sim(**kwargs):
    sims = Simulations.objects(__raw__=kwargs)
    ls = [sim for sim in sims]
    return ls