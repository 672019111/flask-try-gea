// Fungsi untuk menampilkan loading
// Membuat objek tanggal untuk tanggal hari ini
var today = new Date();

// Menghitung jumlah hari dalam bulan ini
var daysInMonth = new Date(today.getFullYear(), today.getMonth() + 1, 0).getDate();

// Menghitung berapa hari lagi untuk akhir bulan
var daysLeft = (daysInMonth + 2) - today.getDate();


function msg(message, type) {
    var alertClass = 'alert-' + type;
    var alert = '<div class="alert ' + alertClass + '" role="alert">' + message + '</div>';
    $('#alert-container').html(alert);

    setTimeout(function () {
        $('#alert-container').empty();
    }, 5000);

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


