FFc = gfortran -c -ffixed-line-length-none -fno-automatic


MAKE = make
LIBDIR = ..
LIB    = libS20_lnx
LIB    = libS20

.f.a:
	${FFc}  $<
	ar rv $@ $*.o
	rm -f $*.o
                                                                                
$(LIBDIR)/$(LIB).a: \
	$(LIBDIR)/$(LIB).a(addata.o) \
	$(LIBDIR)/$(LIB).a(convpack.o) \
	$(LIBDIR)/$(LIB).a(dcopy.o) \
	$(LIBDIR)/$(LIB).a(scopy.o) \
	$(LIBDIR)/$(LIB).a(dot.o) \
	$(LIBDIR)/$(LIB).a(getfdp.o) \
	$(LIBDIR)/$(LIB).a(integ.o) \
	$(LIBDIR)/$(LIB).a(istlen.o) \
	$(LIBDIR)/$(LIB).a(inittrf.o) \
	$(LIBDIR)/$(LIB).a(legndr.o) \
	$(LIBDIR)/$(LIB).a(modtrf.o) \
	$(LIBDIR)/$(LIB).a(rmod.o) \
	$(LIBDIR)/$(LIB).a(saxpy.o) \
	$(LIBDIR)/$(LIB).a(sdot.o) \
	$(LIBDIR)/$(LIB).a(splh.o) \
	$(LIBDIR)/$(LIB).a(strgrep.o) \
	$(LIBDIR)/$(LIB).a(rsphhead.o) \
	$(LIBDIR)/$(LIB).a(rsple.o) \
	$(LIBDIR)/$(LIB).a(rspln.o) \
	$(LIBDIR)/$(LIB).a(splhsetup.o) \
	$(LIBDIR)/$(LIB).a(wsphhead.o) \
	$(LIBDIR)/$(LIB).a(wspthead.o) \
	$(LIBDIR)/$(LIB).a(wint2ch.o) \
	$(LIBDIR)/$(LIB).a(ylm.o)

	ranlib $(LIBDIR)/$(LIB).a
