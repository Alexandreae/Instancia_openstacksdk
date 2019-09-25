import openstack

openstack.enable_logging(debug=True)

conn = openstack.connect(cloud='cloudq')

image = conn.create_image(
    'ubuntu-trusty', filename='ubuntu-trusty.qcow2',wait=True
)

flavor = conn.get_flavor_by_ram(512)

conn.create_server(
    'my-server', image=image, flavor=flavor, wait=True, auto_ip=True
)