# -*- mode: ruby -*-
Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.box_check_update = false

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine. In the example below,
  # accessing "localhost:8080" will access port 80 on the guest machine.
  # config.vm.network "forwarded_port", guest: 80, host: 8080

  config.vm.synced_folder "./", "/home/vagrant/workspace/buddy"

  config.vm.provider "virtualbox" do |vb|
    vb.memory = "1024"
  end

  # hack to go around https://github.com/mitchellh/vagrant/issues/6793
  config.vm.provision :shell, inline: <<-SCRIPT
    GALAXY=/usr/local/bin/ansible-galaxy
    echo '#!/usr/bin/env bash
    /usr/bin/ansible-galaxy "$@"
    exit 0
    ' | sudo tee $GALAXY
    sudo chmod 0755 $GALAXY
  SCRIPT

  config.vm.provision "ansible_local" do |ansible|
      ansible.install        = true
      ansible.playbook       = "setup.yml"
  end
end
