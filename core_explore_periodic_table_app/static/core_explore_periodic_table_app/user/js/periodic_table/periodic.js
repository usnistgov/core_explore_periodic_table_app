/** Search by Periodic Table script **/

let chemical_element_selected = new Array();
const SELECT_ALL_LABEL = "Select All";
const UNSELECT_ALL_LABEL = "Unselect All";
const global_event = {
    input_id: 'id_global_templates',
    button_selector: '.selectAllGlobalTemplateButton'
}

const user_event = {
    input_id: 'id_user_templates',
    button_selector: '.selectAllUserTemplateButton'
}

$( document ).ready(function() {
    let jqElementsField = $("#id_elements");
    let cleanedElementInput = clean_elements_input(jqElementsField.val());
    // bind the event set in the html / bind the event relative to the periodic table
    $("#periodic-clear").on('click', clearPeriodicTableCriteria);
    // init the chemical_element_selected table with the form value
    chemical_element_selected = jqElementsField.val() !== "" ?
        cleanedElementInput.split(",")
        : [];
    /**
     * When click on table's element
     */
    $(document).on('click', '.periodic-table td.p-elem', function(event) {
        let clicked_value = $(this).text();
        let element_index = chemical_element_selected.indexOf(clicked_value);

        if(element_index == -1){
            chemical_element_selected.push(clicked_value);
            $(this).addClass('selected');
        }else{
            chemical_element_selected.splice(element_index, 1);
            $(this).removeClass('selected');
        }

        // update the input value
        jqElementsField.val(chemical_element_selected.join(","));
    });

    // set the element input value
    jqElementsField.val(cleanedElementInput);

    // set the periodic table to the env state
    addSavedQueryToPeriodicTable();
    initSelectAllTemplate();
    initSortingAutoSubmit();
});

/**
 * Initialize select template all button
 */
let initSelectAllTemplate = function() {
    $(".selectAllGlobalTemplateButton").on("click", global_event, selectAllTemplate);
    $(".selectAllUserTemplateButton").on("click", user_event, selectAllTemplate);
    $("input[id^='id_global_templates']").each(function(i) {
        $(this).on("change", global_event, checkIfAllTemplateSelected);
    });
    $("input[id^='id_user_templates']").each(function(i) {
        $(this).on("change", user_event, checkIfAllTemplateSelected);
    });
    checkIfAllTemplateSelected({ data: global_event });
    checkIfAllTemplateSelected({ data: user_event });
}

/**
 * Select all Template function
 */
let selectAllTemplate = function(event) {
    let selectAll = false;
    if ($(event.data.button_selector).html().trim() == SELECT_ALL_LABEL) {
        selectAll = true;
        $(event.data.button_selector).html(UNSELECT_ALL_LABEL);
    } else {
        $(event.data.button_selector).html(SELECT_ALL_LABEL);
    }
    $("input[id^=" + event.data.input_id + "]").each(function(i) {
        $(this).prop("checked", selectAll);
    });
}

/**
 * check if all templates are selected
 */
let checkIfAllTemplateSelected = function(event) {
    let allSelected = true;
    $("input[id^=" + event.data.input_id + "]").each(function(i) {
        if($(this).prop("checked") == false) {
            allSelected = false;
            return false;
        }
    });

    if (allSelected) {
        $(event.data.button_selector).html(UNSELECT_ALL_LABEL);
    } else {
        $(event.data.button_selector).html(SELECT_ALL_LABEL);
    }
}


/**
 * Clear current set of criteria
 */
let clearPeriodicTableCriteria = function(){
    let jqElementsField = $("#id_elements");
    // clear all selection elements
    chemical_element_selected = new Array();
    // remove the selected class for all selected element
    $.each($('.selected'), function(){
        $(this).removeClass('selected');
    });
    // update the input value
    jqElementsField.val(chemical_element_selected.join(","));
    // refresh the result
    submitForm();
};

let initSortingAutoSubmit = function() {
    // waiting for the end of the AJAX call result DOM injection
    let MAX_INTERVAL_ITER = 10;
    let iteration = 0;

    let interval = setInterval(function() {
        iteration++;
        if (iteration >= MAX_INTERVAL_ITER) clearInterval(interval);
        if ($(".filter-dropdown-menu").length > 0) {
            clearInterval(interval);
            $(".dropdown-menu.tools-menu.filter-dropdown-menu li").click(debounce(function() {
                submitForm();
            }, SORTING_SUBMIT_DELAY));
        }
    }, 500);
}

/**
 * Submit the form
 */
let submitForm = function () {
    $("#form_search").submit();
}


/**
 * AJAX call, insert a saved query in the periodic table
 * @param savedQueryID id of the query to insert
 */
let addSavedQueryToPeriodicTable = function(savedQueryID){
    // select periodic table values
    $('.periodic-table tr td').filter(function(){
        if (chemical_element_selected.indexOf($(this).text()) >= 0){
            $(this).addClass('selected');
        }
    });
};


/**
 * Clean the input string
 * @param inputString
 */
let clean_elements_input = (inputString) => {
    let cleanedString = '';
    let splitedElements = inputString.split(",");

    splitedElements.forEach((element, index)=>{
        let splitedElement = element.split(":");

        if(splitedElement && splitedElement.length > 1)
            cleanedString += splitedElement[1];
        else if (splitedElement && splitedElement.length > 0)
            cleanedString += splitedElement[0];

        if (index !== splitedElements.length -1)
            cleanedString += ","
    });

    return cleanedString;
}