
import streamlit as st # type: ignore
from addon_manager import addon_manager

# Configure the main page
st.set_page_config(
    page_title="HomeCore Hub",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar Navigation
st.sidebar.title("🏠 HomeCore")
page = st.sidebar.selectbox("Navigation", ["Dashboard", "Devices", "Integrations", "Settings"])

# Page Content Logic
if page == "Dashboard":
    st.title("🏠 Home Dashboard")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("💡 Lighting")
        if st.button("Toggle Living Room Light"):
            # Placeholder for future API call
            st.success("Command Sent!")

    with col2:
        st.subheader("🌡️ Climate")
        temp = st.slider("Thermostat", 60, 80, 72)
        st.write(f"Target: {temp}°F")

    with col3:
        st.subheader("🔒 Security")
        if st.button("Lock Front Door"):
            st.success("Door Locked!")

elif page == "Devices":
    st.title("🔧 Device Manager")
    st.write("Manage your connected devices here...")
    # Placeholder for device management

elif page == "Integrations":
    st.title("🔌 Integration Store")

    # Load available addons
    available_addons = addon_manager.discover_available()

    if not available_addons:
        st.warning("No addons available yet. Check the 'addons/' directory.")
    else:
        st.subheader("Available Integrations")

        # Create columns for addon cards
        cols = st.columns(min(len(available_addons), 3))

        for i, addon in enumerate(available_addons):
            col_idx = i % 3
            with cols[col_idx]:
                st.info(f"**{addon['name']}**\n{addon['description']}")

                if addon['installed']:
                    st.success("✅ Installed")
                    if st.button(f"Remove {addon['name']}", key=f"remove_{addon['id']}"):
                        addon_manager.uninstall_addon(addon['id'])
                        st.rerun()
                else:
                    if st.button(f"Install {addon['name']}", key=f"install_{addon['id']}"):
                        addon_manager.install_addon(addon['id'])
                        st.rerun()

        # Show installed addons separately
        if addon_manager.installed_addons:
            st.subheader("Installed Integrations")
            for addon_id, info in addon_manager.installed_addons.items():
                st.success(f"✅ {addon_id}")

elif page == "Settings":
    st.title("⚙️ Settings")
    st.write("Configure your HomeCore hub...")
    # Placeholder for settings

# Footer
st.sidebar.divider()
st.sidebar.caption(f"HomeCore v0.1")