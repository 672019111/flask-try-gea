// Fungsi untuk menampilkan loading
function showLoading() {
    $('#loadingModal').modal('show');

}

// Fungsi untuk menclose loading
function hideLoading() {
    console.log ("hide loading")
    // $('#loadingModal').css('display', 'none');
    $('#loadingModal').css('display', 'none');
    // $('body').css('pointer-events', 'auto');
    // $('#loadingModal').css('display', 'block');
    // $('#loadingModal').hide();

    // $('#loadingModal').modal('hide');
    $('.modal-backdrop.fade.show').remove();
}

function msg(message, type) {
    var alertClass = 'alert-' + type;
    var alert = '<div class="alert ' + alertClass + '" role="alert">' + message + '</div>';
    $('#alert-container').html(alert);
}

const terbilang = (number) => {
    if (!number) {
        return "";
    }
    const bilangan = [
        "", "satu", "dua", "tiga", "empat", "lima", "enam", "tujuh", "delapan", "sembilan", "sepuluh", "sebelas"
    ];

    if (number < 12) {
        return bilangan[number];
    } else if (number < 20) {
        return bilangan[number - 10] + " belas";
    } else if (number < 100) {
        return (
            bilangan[Math.floor(number / 10)] +
            " puluh " +
            bilangan[number % 10]
        );
    } else if (number < 200) {
        return "seratus " + terbilang(number - 100);
    } else if (number < 1000) {
        return (
            bilangan[Math.floor(number / 100)] +
            " ratus " +
            terbilang(number % 100)
        );
    } else if (number < 2000) {
        return "seribu " + terbilang(number - 1000);
    } else if (number < 1000000) {
        return (
            terbilang(Math.floor(number / 1000)) +
            " ribu " +
            terbilang(number % 1000)
        );
    } else if (number < 1000000000) {
        return (
            terbilang(Math.floor(number / 1000000)) +
            " juta " +
            terbilang(number % 1000000)
        );
    } else if (number >= 1000000000) {
        return "Angka terlalu besar";
    }
}


