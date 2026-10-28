import os
import shutil
import glob

ROOT = "f:/chrome/stitch_plant_store_website_landing/stitch_plant_store_website_landing"

RAW_FOLDERS = [
    '30_day_root_vitality_checkup_appointment_confirmation',
    '30_day_root_vitality_checkup_booking_acclimation_log',
    'a_close_up_high_definition_smartphone_camera_feed_of_a_person_unboxing_a',
    'archival_envelope_mailing_label_template',
    'botanical_boutique',
    'botanical_boutique_plant_storefront',
    'botanical_certificate_invoice_dedicated_print_preview_mode',
    'botanical_checkout_add_card_split_payment_modal',
    'botanical_checkout_add_new_card_modal_state',
    'botanical_checkout_multi_step_greenhouse_dispatch',
    'botanical_checkout_order_processing_settlement_success',
    'botanical_checkout_order_review_final_confirmation',
    'botanical_checkout_payment_settlement',
    'botanical_invoice_certificate_of_provenance',
    'botanical_order_confirmation_specimen_dispatch_tracker',
    'cart_checkout_drawer_customized_monstera_deliciosa',
    'client_feedback_botanical_specimen_reviews',
    'conservatory_care_lab_foliar_diagnostic_tool',
    'curated_botanical_catalog_specimen_archive',
    'horticulturist_video_consultation_specimen_unboxing_scheduling',
    'live_horticulturist_video_consultation_root_health_audit',
    'living_plant_passport_digital_herbarium',
    'monstera_deliciosa_plant_detail_pot_customizer',
    'professional_split_screen_video_call_interface_view_master_botanist_dr_elena',
    'sanctuary_portal_account_created_welcome_state',
    'sanctuary_portal_create_account_specimen_linking',
    'sanctuary_portal_mobile_welcome_account_state',
    'sanctuary_portal_sign_in_account_creation'
]

SCREENSHOT_MAPPING = [
    ('01_botanical_boutique_plant_storefront.png', 'botanical_boutique_plant_storefront', 'Storefront Homepage'),
    ('02_curated_botanical_catalog_specimen_archive.png', 'curated_botanical_catalog_specimen_archive', 'Curated Botanical Catalog'),
    ('03_monstera_deliciosa_plant_detail_pot_customizer.png', 'monstera_deliciosa_plant_detail_pot_customizer', 'Monstera Pot Customizer'),
    ('04_cart_checkout_drawer_customized_monstera.png', 'cart_checkout_drawer_customized_monstera_deliciosa', 'Cart Drawer & Thermal Packaging'),
    ('05_botanical_checkout_multi_step_greenhouse_dispatch.png', 'botanical_checkout_multi_step_greenhouse_dispatch', 'Greenhouse Dispatch Checkout (Step 1)'),
    ('06_botanical_checkout_payment_settlement.png', 'botanical_checkout_payment_settlement', 'Payment Settlement (Step 2)'),
    ('07_botanical_checkout_add_new_card_modal_state.png', 'botanical_checkout_add_new_card_modal_state', 'Add Card Modal State'),
    ('08_botanical_checkout_add_card_split_payment_modal.png', 'botanical_checkout_add_card_split_payment_modal', 'Split Payment Settlement Modal'),
    ('09_botanical_checkout_order_review_final_confirmation.png', 'botanical_checkout_order_review_final_confirmation', 'Order Review & Settlement (Step 3)'),
    ('10_botanical_checkout_order_processing_settlement_success.png', 'botanical_checkout_order_processing_settlement_success', 'Order Processing & Settlement Success (Step 4)'),
    ('11_botanical_order_confirmation_specimen_dispatch_tracker.png', 'botanical_order_confirmation_specimen_dispatch_tracker', 'Specimen Dispatch Tracker & Telemetry'),
    ('12_botanical_invoice_certificate_of_provenance.png', 'botanical_invoice_certificate_of_provenance', 'Archival Invoice & Certificate of Provenance'),
    ('13_botanical_certificate_invoice_dedicated_print_preview_mode.png', 'botanical_certificate_invoice_dedicated_print_preview_mode', 'Dedicated Archival Print Mode'),
    ('14_archival_envelope_mailing_label_template.png', 'archival_envelope_mailing_label_template', 'Greenhouse Archival Mailing Label'),
    ('15_conservatory_care_lab_foliar_diagnostic_tool.png', 'conservatory_care_lab_foliar_diagnostic_tool', 'Conservatory Care Lab & Foliar Diagnostic'),
    ('16_living_plant_passport_digital_herbarium.png', 'living_plant_passport_digital_herbarium', 'Living Plant Passport & Herbarium'),
    ('17_horticulturist_video_consultation_specimen_unboxing_scheduling.png', 'horticulturist_video_consultation_specimen_unboxing_scheduling', '1:1 Video Consultation Scheduling'),
    ('18_live_horticulturist_video_consultation_root_health_audit.png', 'live_horticulturist_video_consultation_root_health_audit', 'Live Consultation Root Health Audit'),
    ('19_professional_split_screen_video_call_interface_view_master_botanist.png', 'professional_split_screen_video_call_interface_view_master_botanist_dr_elena', 'Split-Screen Tele-Horticulture Call Room'),
    ('20_a_close_up_high_definition_smartphone_camera_feed.png', 'a_close_up_high_definition_smartphone_camera_feed_of_a_person_unboxing_a', 'Foliar Camera Feed Macro Unboxing'),
    ('21_30_day_root_vitality_checkup_booking_acclimation_log.png', '30_day_root_vitality_checkup_booking_acclimation_log', '30-Day Root Vitality Checkup Booking'),
    ('22_30_day_root_vitality_checkup_appointment_confirmation.png', '30_day_root_vitality_checkup_appointment_confirmation', 'Root Vitality Checkup Confirmed'),
    ('23_client_feedback_botanical_specimen_reviews.png', 'client_feedback_botanical_specimen_reviews', 'Client Feedback & Botanical Reviews'),
    ('24_sanctuary_portal_sign_in_account_creation.png', 'sanctuary_portal_sign_in_account_creation', 'Sanctuary Portal Sign In'),
    ('25_sanctuary_portal_create_account_specimen_linking.png', 'sanctuary_portal_create_account_specimen_linking', 'Specimen Passport Linking'),
    ('26_sanctuary_portal_account_created_welcome_state.png', 'sanctuary_portal_account_created_welcome_state', 'Member Dashboard Welcome State'),
    ('27_sanctuary_portal_mobile_welcome_account_state.png', 'sanctuary_portal_mobile_welcome_account_state', 'Mobile Welcome Account State')
]

def organize():
    # 1. Create inner folders
    screenshots_dir = os.path.join(ROOT, "screenshots")
    raw_designs_dir = os.path.join(ROOT, "raw_stitch_designs")
    scripts_dir = os.path.join(ROOT, "scripts")

    os.makedirs(screenshots_dir, exist_ok=True)
    os.makedirs(raw_designs_dir, exist_ok=True)
    os.makedirs(scripts_dir, exist_ok=True)

    print("Created inner directories: screenshots, raw_stitch_designs, scripts")

    # 2. Copy and rename all screenshots to screenshots/
    copied_count = 0
    gallery_items = []

    for dest_name, src_folder, title in SCREENSHOT_MAPPING:
        src_file = os.path.join(ROOT, src_folder, "screen.png")
        if os.path.exists(src_file):
            dest_file = os.path.join(screenshots_dir, dest_name)
            shutil.copy2(src_file, dest_file)
            copied_count += 1
            gallery_items.append((dest_name, title, src_folder))
            print(f"Copied screenshot: {dest_name}")
        else:
            print(f"Warning: {src_file} does not exist!")

    print(f"Total screenshots organized: {copied_count}/27")

    # 3. Create visual HTML screenshot gallery inside screenshots/index.html
    gallery_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Verdant Haven — Original Design Screenshots Gallery</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,500;0,600;1,500&family=Plus+Jakarta+Sans:wght@400;500;600;700&family=Material+Symbols+Outlined&display=swap" rel="stylesheet">
  <style>
    body {{ font-family: 'Plus Jakarta Sans', sans-serif; background: #faf9f4; color: #1b1c19; }}
    h1, h2, h3 {{ font-family: 'Playfair Display', serif; }}
  </style>
</head>
<body class="p-6 md:p-12 max-w-7xl mx-auto">
  <header class="mb-10 pb-6 border-b border-[#003629]/15 flex flex-col md:flex-row items-start md:items-center justify-between gap-4">
    <div>
      <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-[#1b4d3e]/10 text-[#003629] text-xs font-bold uppercase tracking-widest mb-2">
        <span class="material-symbols-outlined text-[16px]">photo_library</span>
        <span>Original Design Archive</span>
      </div>
      <h1 class="text-3xl md:text-4xl text-[#003629] font-bold">Verdant Haven Design Mockups &amp; Screenshots</h1>
      <p class="text-sm text-[#404945] mt-1">Catalog of all 27 original design screens shared for the botanical atelier &amp; nursery sanctuary.</p>
    </div>
    <div class="flex items-center gap-3">
      <a href="../index.html" class="px-5 py-2.5 rounded-xl bg-[#003629] text-white text-xs font-bold shadow hover:bg-[#1b4d3e] transition-all flex items-center gap-2">
        <span class="material-symbols-outlined text-[18px]">storefront</span>
        <span>Open Functional Website</span>
      </a>
    </div>
  </header>

  <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
    {"".join(f"""
    <div class="bg-white rounded-2xl shadow-sm hover:shadow-lg border border-[#003629]/10 overflow-hidden transition-all group flex flex-col justify-between">
      <div class="relative aspect-[16/10] bg-neutral-100 overflow-hidden">
        <img src="{img}" alt="{title}" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" loading="lazy" />
        <span class="absolute top-3 left-3 px-2.5 py-1 rounded-full bg-[#003629]/80 backdrop-blur text-white text-[11px] font-bold font-mono">#{idx+1:02d}</span>
      </div>
      <div class="p-4 flex flex-col gap-2">
        <h3 class="text-base font-bold text-[#003629] leading-snug">{title}</h3>
        <p class="text-xs text-[#707974] font-mono truncate">{img}</p>
        <div class="flex items-center justify-between pt-2 border-t border-neutral-100">
          <span class="text-[11px] text-[#50652a] font-semibold">{folder}</span>
          <a href="{img}" target="_blank" class="text-xs font-bold text-[#003629] hover:underline flex items-center gap-1">
            <span>View Full Size</span>
            <span class="material-symbols-outlined text-[14px]">open_in_new</span>
          </a>
        </div>
      </div>
    </div>
    """ for idx, (img, title, folder) in enumerate(gallery_items))}
  </div>
</body>
</html>
'''
    with open(os.path.join(screenshots_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(gallery_html)
    print("Created screenshots/index.html visual gallery!")

    # 4. Move 28 raw design folders into raw_stitch_designs/
    moved_folders = 0
    for folder_name in RAW_FOLDERS:
        src = os.path.join(ROOT, folder_name)
        dest = os.path.join(raw_designs_dir, folder_name)
        if os.path.exists(src) and not os.path.exists(dest):
            shutil.move(src, dest)
            moved_folders += 1
            print(f"Moved raw design folder: {folder_name} -> raw_stitch_designs/")
        elif os.path.exists(dest):
            print(f"Already in raw_stitch_designs: {folder_name}")

    print(f"Total raw folders moved: {moved_folders}/28")

    # 5. Move python build & migration scripts into scripts/
    python_scripts = [
        'build_all_pages.py', 'build_full_website.py', 'build_site.py',
        'clean_social.py', 'enhance_account_link.py', 'enhance_care_lab.py',
        'enhance_dashboard.py', 'enhance_invoice.py', 'enhance_nav_layout.py',
        'enhance_passport.py', 'enhance_reviews.py', 'enhance_video_call.py',
        'inspect_site.py', 'patch_links.py', 'patch_remaining_links.py'
    ]

    moved_scripts = 0
    for script_name in python_scripts:
        src = os.path.join(ROOT, script_name)
        dest = os.path.join(scripts_dir, script_name)
        if os.path.exists(src) and not os.path.exists(dest):
            shutil.move(src, dest)
            moved_scripts += 1
            print(f"Moved script: {script_name} -> scripts/")

    print(f"Total scripts moved: {moved_scripts}")

if __name__ == '__main__':
    organize()
