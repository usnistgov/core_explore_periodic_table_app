var chimical_element_selected = new Array();

$( document ).ready(function() {
    // unbind the event set in the html / bind the event relative to the periodic table
    $("#queryBuilder .btn-danger").attr('onclick', "").click(clearPeriodicTableCriteria);
    $("#queryBuilder .btn-secondary").attr('onclick', "").click(savePeriodicTableQuery);
    $("#queryBuilder .btn-primary").attr('onclick', "").click(submitPeriodicTableQuery);
    setOnclickActionForQueryTableButtons();
});

/**
 * When click on table's element
 */
$(document).on('click', '.periodic-table td.p-elem', function(event) {
    var clicked_value = $(this).text();
    var element_index = chimical_element_selected.indexOf(clicked_value);
    if(element_index == -1){
        chimical_element_selected.push(clicked_value);
        $(this).addClass('selected');
    }else{
        chimical_element_selected.splice(element_index, 1);
        $(this).removeClass('selected');
    }
});


/**
 * AJAX call, clear current set of criteria
 */
var clearPeriodicTableCriteria = function(){
    // clear all selection elements
    chimical_element_selected = new Array();
    // remove the selected class for all selected element
    $.each($('.selected'), function(){
        $(this).removeClass('selected');
    });
};


/**
 * AJAX call, save the query
 */
var savePeriodicTableQuery = function(){
    $.ajax({
        url : savePeriodicTableUrlQueryUrl,
        type : "POST",
        dataType: "json",
        data : {
        	'periodic_table_values': JSON.stringify(chimical_element_selected)
        },
        success: function(data){
            $('#queriesTable').load(reloadBuildQueryUrl +  ' #queriesTable', function() {
                setOnclickActionForQueryTableButtons();
            });
            clearPeriodicTableCriteria();
        },
        error: function(data){
            showErrorModal(data.responseText);
        }
    });
};


/**
 * AJAX call, insert a saved query in the periodic table
 * @param savedQueryID id of the query to insert
 */
var addSavedQueryToPeriodicTable = function(savedQueryID){
    $.ajax({
        url : getSavedQueryValuesUrl,
        type : "GET",
        dataType: "json",
        data : {
        	savedQueryID: savedQueryID
        },
        success: function(data){
            // select periodic table values
            $('.periodic-table tr td').filter(function(){
                if (data.indexOf($(this).text()) >= 0){
                    $(this).addClass('selected');
                }
            });

            // re init the list and populate him with all values
            chimical_element_selected = new Array();
            $.each($('.periodic-table .selected'), function(index, element){
                chimical_element_selected.push($(element).text());
            });
        }
    });
};

/**
 * set all onclick button of save queries table
 */
var setOnclickActionForQueryTableButtons = function() {
    $("#queriesTable span.fa-arrow-circle-up").each(function (index, element) {
        var attr_value = $(element).attr('onclick');
        $(element).attr('onclick', attr_value.replace("addSavedQueryToForm", "addSavedQueryToPeriodicTable"));
    });
};


/**
 * AJAX call, execute query and redirects to result page
 */
var submitPeriodicTableQuery = function(){
    var queryID = $("#query_id").html();

    // get query from form
    $.ajax({
        url : submitQueryUrl,
        type : "POST",
        dataType: "json",
        data : {
            'selectedValues': JSON.stringify(chimical_element_selected),
            'queryID': queryID
        },
        success: function(data){
            window.location = resultsUrl;
        },
        error: function(data){
            showErrorModal(data.responseText);
        }
    });
};
