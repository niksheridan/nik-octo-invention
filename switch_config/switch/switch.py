#!/usr/bin/env python
import json
import yaml
from jinja2 import Environment, PackageLoader, FileSystemLoader
from pprint import pprint


class Switch:

    def __init__(self, device_templates, device_vars):
        '''
        create the basics to pass to the methods with the object
        '''
        self.switch_templates = device_templates
        self.switch_variables = device_vars
        self.switch_vars = self.yaml2dict(device_vars)
        self.template_access_port = 'switchport_access.j2'
        self.template_crosslink_ports = 'switchport_crosslink.j2'
        self.template_authentication = 'authentiction.j2'

    def yaml2dict(self, yaml_file):
        '''
		load yaml file into dictionary list, and pretty print to demonstrate success
		'''
        with open(yaml_file, 'r') as stream:
            try:
                var_dict = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)
        return var_dict

    def show_attributes(self):
        '''
        method used only to output the varibles passed to the
        class when the object is created
        '''
        pprint(self.switch_vars)

    def access_ports(self):
        '''
        load a template and render it
        (need to make more generic for reusability)
        '''
        # sets the environment where the templates are stored: a folder in this case called 'templates'
        template_env = Environment(
            loader=FileSystemLoader(self.switch_templates), trim_blocks=True
            )
        template = template_env.get_template(self.template_access_port)
        for switchport in self.switch_vars['switch']['access_ports']:
            rendered_template = template.render(
            switchport=switchport['port'],
            switchport_description=self.switch_vars['switch'][
            'access_port_description'],
            switchport_vlan=switchport['access_vlan'],
            switchport_voice_vlan=switchport['voice_vlan'])
        print(rendered_template)

    def crosslink_ports(self):
        '''
		load a template and render it
		(need to make more generic for reusability)
		'''
        # sets the environment where the templates are stored: a folder in this case called 'templates'
        template_env = Environment(
        loader=FileSystemLoader(self.switch_templates), trim_blocks=True)
        template = template_env.get_template(self.template_crosslink_ports)
        for switchport in self.switch_vars['switch']['crosslink_ports']:
            rendered_template = template.render(
                switchport=switchport['port'],
                switchport_description=switchport['description'],
                switchport_native_vlan=switchport['native_vlan'],
                switchport_vlan=switchport['crosslink_port_description'],
                switchport_voice_vlan=switchport['allowed_vlans']
            )
        print(rendered_template)

    def uplink_ports(self):
        '''
		load a template and render it
		(need to make more generic for reusability)
		'''
        # sets the environment where the templates are stored: a folder in this case called 'templates'
        template_env = Environment(
        loader=FileSystemLoader(self.switch_templates), trim_blocks=True)
        template = template_env.get_template(self.template_access_port)
        for switchport in self.switch_vars['switch']['uplink_ports']:
            rendered_template = template.render(
                switchport=switchport['port'], switchport_vlan=switchport['vlan']
            )
        print(rendered_template)

    def downlink_ports(self):
        '''
		load a template and render it
		(need to make more generic for reusability)
		'''
        # sets the environment where the templates are stored: a folder in this case called 'templates'
        template_env = Environment(
            loader=FileSystemLoader(self.switch_templates), trim_blocks=True
        )
        template = template_env.get_template(self.template_access_port)
        for switchport in self.switch_vars['switch']['downlink_ports(']:
            rendered_template = template.render(
            switchport1=switchport['port'], switchport_vlan=switchport['vlan'])
        print(rendered_template)

    def authentication(self):
        pass
        ##self.accessports_range[0],self.accessports_range[1],self.accessports_range[2]):
        #rendered_template = template.render(
        #    primary_tacacs='GigabitEthernet1/0/' + str(switchport),
        #    seconday_tacacs='300'
        #)
        #print(rendered_template)