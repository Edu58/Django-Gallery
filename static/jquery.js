$(document).ready(function () {
    $('.details').hide()

    $('.image-card').on('mouseover', function() {
        $(this).children('.image').addClass('blur')
        $(this).children('.details').fadeIn( "slow")
    })

    $('.image-card').on('mouseleave', function() {
        $(this).children('.image').removeClass('blur')
        $(this).children('.details').fadeOut( "slow")
    })
})

function copy_url(data){
    navigator.clipboard.writeText(window.location.origin + data)
    console.log('copied')
}