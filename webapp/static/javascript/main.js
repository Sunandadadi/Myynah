$( document ).ready(function() {

    function floatSearchOnTop() {
        $('#search-tag').removeClass('padding-left-right-25vh padding-top-35vh');
        $('#search-tag').addClass("none-display");
        $('#search-bar').addClass('margin-top-3');
    }

    function clearPreviousSearch() {
        $('.search-results').remove();
    }

    function setloader() {
        $('#page-content').addClass("none-display");
        $('#loader').removeClass("none-display").addClass("block-display");
    }

    function resetloader() {
        $('#loader').removeClass("block-display").addClass("none-display");
        $('#page-content').removeClass("none-display").addClass("block-display");
    }

    $(document).on('click', '.search-partners-btn', function() {
        setloader();
        clearPreviousSearch();
        var search_input = $('.search-input').val().toLowerCase().trim();
        if (!search_input) {
            return;
        };
        $.ajax({
            url: 'http://localhost:8080/search_partners/' + search_input,
            type: 'GET',
            dataType: 'html'
        }).then(function(data) {
            floatSearchOnTop();
            resetloader();
            $('#page-content').append(data);
        });;
    });

    $(document).on('keypress', '.search-input', function(e) {
        if (e.which == 13) {
            $('.search-partners-btn').click();
        }
    });

    $(document).on('click', '.about-btn', function() {
        $.ajax({
            url: 'http://localhost:8080/about',
            type: 'GET',
            dataType: 'html'

        }).then(function(data) {
            $('#page-content').html(data);
        });;
    });

    $(document).on('click', '.brand-tag', function() {
        location.reload();
    });

    $(document).on('click', '.accordion', function() {
        $(this).find('.accordion-arrow').toggleClass('fa-angle-down fa-angle-up');
    });

});
