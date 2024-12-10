# Set PERL, TABLEVIEWER_DIR, CIRCOS_DIR and WORKING_DIR variables based on you system.
cd WORKING_DIR
$PERL $TABLEVIEWER_DIR/bin/parse-table -conf etc/parse-table.conf -file uploads/table.txt -max_col_num 40 -max_row_num 40 -segment_order=ascii,size_desc -placement_order=row,col -interpolate_type count -color_source row -transparency 1 -fade_transparency 0 -ribbon_layer_order=size_asc > data/parsed.txt 2> WORKING_DIR/data/stderr.txt
cat data/parsed.txt | $TABLEVIEWER_DIR/bin/make-conf -dir data
$PERL $CIRCOS_DIR/bin/circos -param random_string=smxxjse -conf etc/circos.conf
cd WORKING_DIR; PERL CIRCOS_DIR/bin/circos -param random_string=smxxjse -conf WORKING_DIR/etc/circos.conf 2>&1 > WORKING_DIR/results/report.txt
tar cvfz circos-tableviewer-smxxjse.tar.gz *
