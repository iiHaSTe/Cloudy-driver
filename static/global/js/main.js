// nvigation button
$("#nav-btn").click(function() {
    $(this.dataset.target).toggleClass('hidden');
    /*
     * hidden class will slide menu to right
     */
});

// get all list from menu
$('.nav-body ul li').each((index, el) => {
    $(el).click(function() {
        // now li will work like anchor tag
        location.href = $(this).attr('href');
    });
});
