from django.db import models

class MonthYear(models.Model):
    MONTHYEAR = (
        ('Januari 2020', 'Januari 2020'),
        ('Februari 2020', 'Februari 2020'),
        ('Maret 2020', 'Maret 2020'),
        ('April 2020', 'April 2020'),
        ('Mei 2020', 'Mei 2020'),
        ('Juni 2020', 'Juni 2020'),
        ('Juli 2020', 'Juli 2020'),
        ('Agustus 2020', 'Agustus 2020'),
        ('September 2020', 'September 2020'),
        ('Oktober 2020', 'Oktober 2020'),
        ('November 2020', 'November 2020'),
        ('Desember 2020', 'Desember 2020'),
    )

    monthYear = models.CharField(max_length=200, null=True, choices=MONTHYEAR)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    # output name di list model(database) customer
    def __str__(self):
        return self.monthYear


class Budget(models.Model):
    STATUS = (
        ('Pemasukan', 'Pemasukan'),
        ('Pengeluaran', 'Pengeluaran')
    )

    namaAksi = models.CharField(max_length=200, null=True)
    monthYear = models.ForeignKey(MonthYear, null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    totalBiaya = models.IntegerField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.namaAksi


