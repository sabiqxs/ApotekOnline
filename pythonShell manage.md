directori project in cmd

    python manage.py shell
di shell
   
    >>from megapotek.models import DataObat

menampilkan data
    
    >>DataObat.objects.all()

melihat data berdasarkan filter

    >>DataObat.objects.filter(title__icontains="batuk")

menambahkan database

    >>DataObat.objects.create(title='Obat Baru', content='new Obat', price=40000)
    
    >> queryset = DataObat.objects.all()
    >>> for obj in queryset:
    ...     print (obj.title)
    ...     print (obj.content)
    ...     print (obj.updated)
    ...     print (obj.price)
    ...     print (obj.timestamp)
    ...     print (obj.id)
    ...     print (obj.pk)