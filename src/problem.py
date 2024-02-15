import streamlit as st
import zipfile
import os
import json

def validate_zip_structure(zip_obj):
    """
    validates if the zip file contains the required structure.
    """
    expected_files = {"/description.md", "/metadata.json"}
    expected_dirs = {"testcases/"}
    found_files = set()
    found_dirs = set()

    parent_directory = None
    for info in zip_obj.infolist():
        if parent_directory is None:
            parent_directory = info.filename.split('/')[0] + '/' 
            continue  

        adjusted_filename = info.filename[len(parent_directory):]

        if adjusted_filename.endswith("/"):
            found_dirs.add(adjusted_filename)
        else:
            dirname, filename = os.path.split(adjusted_filename)
            if dirname == "":
                found_files.add("/" + filename)  
            elif dirname == "testcases":
                if filename.startswith("input") or filename.startswith("output"):
                    found_dirs.add(dirname + "/")
    
    print(found_files, found_dirs)

    return expected_files <= found_files and expected_dirs <= found_dirs



def extract_and_process_files(zip_obj):
    """
    extracts and processes the files from zip.
    displays description, metadata and test cases.
    """
    description_content = None
    metadata_content = None
    test_cases_count = 0

    parent_directory = zip_obj.namelist()[0].split('/')[0] + '/'  

    for info in zip_obj.infolist():
        adjusted_filename = info.filename[len(parent_directory):]

        if adjusted_filename == "description.md":
            with zip_obj.open(info) as file:
                description_content = file.read().decode('utf-8')
        elif adjusted_filename == "metadata.json":
            with zip_obj.open(info) as file:
                metadata_content = json.load(file)
        elif adjusted_filename.startswith("testcases/"):
            if adjusted_filename.split('/')[1].startswith(("input", "output")):
                test_cases_count += 1

    return description_content, metadata_content, test_cases_count


st.title("Problem Importer")

uploaded_file = st.file_uploader("Choose a zip file", type="zip")

if uploaded_file is not None:
    with zipfile.ZipFile(uploaded_file, 'r') as zip_ref:
        if validate_zip_structure(zip_ref):
            st.success("Valid zip structure. Processing...")
            description, metadata, test_cases_count = extract_and_process_files(zip_ref)
            
            if description:
                st.subheader("Description")
                st.markdown(description)
            
            if metadata:
                st.subheader("Metadata")
                st.json(metadata)
            
            st.subheader("Test Cases")
            st.write(f"Found {test_cases_count} test cases.")
            
        else:
            st.error("Invalid zip file structure.")
