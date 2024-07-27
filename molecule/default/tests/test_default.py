def test_kvm_installed(host):
    # Check if KVM packages are installed
    kvm = host.package("qemu-kvm")
    assert kvm.is_installed

    libvirt = host.package("libvirt")
    assert libvirt.is_installed

    virt_manager = host.package("virt-manager")
    assert virt_manager.is_installed

def test_libvirtd_running_and_enabled(host):
    # Check if libvirtd service is running and enabled
    libvirtd = host.service("libvirtd")
    assert libvirtd.is_running
    assert libvirtd.is_enabled

def test_network_bridge_exists(host):
    # Check if the network bridge is created
    bridge = host.interface("virbr0")
    assert bridge.exists
    assert bridge.is_up