AutoDeclare Vector v;
Local F1 = i_^2*dd_(v1,v4,v2,v2,v2,v2,v3,v3,v3,v3);
Local F2 = 1-i_*dd_(v2,v2,v2,v2)-i_^2/2*dd_(v2,v2,v2,v2,v3,v3,v3,v3);
Print +s F1 F2;
.end
