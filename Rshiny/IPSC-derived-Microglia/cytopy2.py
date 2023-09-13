#!/usr/bin/env python
# coding: utf-8

def gcyto(tlist):
    import xlrd
    import matplotlib.pyplot as plt
    from matplotlib.cm import ScalarMappable
    sheet = xlrd.open_workbook('ms.xls').sheet_by_index(0)
    cytokine=sheet.col_values(4)[1:71]
    pval=sheet.col_values(5)[1:71]
    l2fc=sheet.col_values(6)[1:71]
    data_x=[]
    data_hight=[]
    data_color=[]
    for k in range(len(cytokine)):
        if cytokine[k] in tlist:
            data_x.append(cytokine[k])
            data_hight.append(l2fc[k])
            data_color.append(pval[k])
    data_color_normalized = [x / max(data_color) for x in data_color]
    fig, ax = plt.subplots(figsize=(13, 10))
    my_cmap = plt.cm.get_cmap('jet')
    colors = my_cmap(data_color_normalized)
    rects = ax.bar(data_x, data_hight, color=colors)
    sm = ScalarMappable(cmap=my_cmap, norm=plt.Normalize(min(data_color),max(data_color)))
    cbar = plt.colorbar(sm)
    cbar.set_label('-log10(p-value)', rotation=270,labelpad=25)   
    plt.ylabel("log2fc")
    ax.set_xticklabels(data_x, rotation = 90, fontsize=7)
    plt.xlabel("Cytokines")
    plt.savefig('cytoplot.png')
def gms(tlist):
    import xlrd
    import matplotlib.pyplot as plt
    sheet = xlrd.open_workbook('ms.xls').sheet_by_index(0)
    gene=sheet.col_values(0)[1:]
    pmg=sheet.col_values(1)[1:]
    img1=sheet.col_values(2)[1:]
    img2=sheet.col_values(3)[1:]
    genef=[]
    pmgf=[]
    img1f=[]
    img2f=[]
    for k in range(len(gene)):
        if gene[k] in tlist:
            genef.append(gene[k])
            pmgf.append(pmg[k])
            img1f.append(img1[k])
            img2f.append(img2[k])
    barWidth = 0.2
    fig, ax = plt.subplots(figsize =(13, 10))
    br1 = [k for k in range(len(pmgf))]
    br2 = [x + barWidth for x in br1]
    br3 = [x + barWidth for x in br2]
    plt.bar(br1, pmgf, color ='lime', width = barWidth,
        edgecolor ='grey', label ='pMG')
    plt.bar(br2, img1f, color ='royalblue', width = barWidth,
        edgecolor ='grey', label ='PASEF')
    plt.bar(br3, img2f, color ='blueviolet', width = barWidth,
        edgecolor ='grey', label ='diaPASEF')
    plt.xlabel('Gene', fontweight ='bold', fontsize = 15)
    plt.ylabel('Normalized Intensity', fontweight ='bold', fontsize = 15)
    plt.xticks([r+barWidth for r in range(len(pmgf))],genef)
    ax.set_xticklabels(genef, rotation = 90, fontsize=7)
    plt.legend()
    plt.savefig('msplot.png')
