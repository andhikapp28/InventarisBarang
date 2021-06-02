function cetakPDF(){
    const element = document.getElementById("laporan");

    html2pdf()
    .from(element)
    .save();

}