import openstack

openstack.enable_logging(debug=True)

conn = openstack.connect(cloud='cloudq')

image = conn.get_image('bionic')

flavor = conn.get_flavor_by_ram(1024)

conn.create_server(
    'my-server', image=image, flavor=flavor, wait=True, auto_ip=True, network='internal'
)

#para deletar o server, rodar openstack server delete my-server
