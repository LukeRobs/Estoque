$(document).ready(function () {
    //insert class in the first product item
    $('#id_estoque-0-produto').addClass('clProduto');
    $('#id_estoque-0-quantidade').addClass('clQuantidade');

    // disable the first balance field
    $('#id_estoque-0-saldo').prop('type', 'hidden')
    // creates a span to show the balance on the screen
    $('label[for="id_estoque-0-saldo"]').append('<span id="id_estoque-0-saldo-span" class="lead" style="padding-left: 10px;"></span')

    $('#add-item').click(function (ev) {
        ev.preventDefault();
        var count = $('#estoque').children().length;
        var tmplMarkup = $('#item-estoque').html()
        var compiledTmpl = tmplMarkup.replace(/__prefix__/g, count);
        $('div#estoque').append(compiledTmpl)

        // update form count
        $('#id_estoque-TOTAL_FORMS').attr('value', count + 1);

        // disable the balance
        $('#id_estoque-' + (count) + '-saldo').prop('type', 'hidden')

        // some animate to scroll to view our new form
        $('html, body').animate({
            scrollTop: $("#add-item").position().top - 200
        }, 800);

        $('#id_estoque-' + (count) + '-produto').addClass('clProduto');
        $('#id_estoque-' + (count) + '-quantidade').addClass('clQuantidade');
        // creates a span to show the balance on the screen
        $('label[for="id_estoque-' + (count) + '-saldo"]').append('<span id="id_estoque-' + (count) + '-saldo-span" class="lead" style="padding-left: 10px;"></span')
    });
});


let estoque
let saldo
let campo
let campo2
let quantidade

$(document).on('change', '.clProduto', function () {
    let self = $(this)
    let pk = $(this).val()
    let url = '/produto/' + pk + '/json/'

    $.ajax({
        url: url,
        type: 'GET',
        success: function (response) {
            estoque = response.data[0].estoque
            campo = self.attr('id').replace('produto', 'quantidade')
            // Removes the value from the 'quantity' field
            $('#' + campo).val('')
        },
        error: function (xhr) {
           
        }
    })
});

$(document).on('change', '.clQuantidade', function () {
    quantidade = $(this).val();
    // performs the calculation of the sum of stock
    saldo = Number(estoque) - Number(quantidade);
    campo = $(this).attr('id').replace('quantidade', 'saldo')
    if (saldo < 0) {
        alert('O saldo não pode ser negativo')
        $('#' + campo).val('')
        return
    }
    // Assign the balance to the 'balance' field
    $('#' + campo).val(saldo)
    campo2 = $(this).attr('id').replace('quantidade', 'saldo-span')
    // assigns the balance to the 'id_estoque-x-saldo-span' field
    $('#' + campo2).text(saldo)
});